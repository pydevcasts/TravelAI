import joblib
import numpy as np
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import BostonHousing  # Import your model
from .serializers import BostonHousingSerializer  # Import your serializer

# Load your model (make sure the path is correct)
model = joblib.load("boston_housing_model.pkl")


class BostonHousingListCreateView(generics.ListCreateAPIView):
    queryset = BostonHousing.objects.all()
    serializer_class = BostonHousingSerializer
    permission_classes = [IsAuthenticated]  # Set permission classes

    def post(self, request, *args, **kwargs):
        # Use the serializer to validate input data
        serializer = BostonHousingSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Extract validated data
        validated_data = serializer.validated_data

        # Prepare input data for prediction
        input_data = np.array(
            [
                [
                    validated_data["crim"],
                    validated_data["zn"],
                    validated_data["indus"],
                    validated_data["chas"],
                    validated_data["nox"],
                    validated_data["rm"],
                    validated_data["age"],
                    validated_data["dis"],
                    validated_data["rad"],
                    validated_data["tax"],
                    validated_data["ptratio"],
                    validated_data["b"],
                    validated_data["lstat"],
                ]
            ]
        )

        try:
            # Make prediction
            predicted_price = model.predict(input_data)

            # Save the prediction along with input data to the database
            prediction_instance = BostonHousing.objects.create(
                crim=validated_data["crim"],
                zn=validated_data["zn"],
                indus=validated_data["indus"],
                chas=validated_data["chas"],
                nox=validated_data["nox"],
                rm=validated_data["rm"],
                age=validated_data["age"],
                dis=validated_data["dis"],
                rad=validated_data["rad"],
                tax=validated_data["tax"],
                ptratio=validated_data["ptratio"],
                b=validated_data["b"],
                lstat=validated_data["lstat"],
                medv=predicted_price[0],  # Save the predicted price
            )

            return Response(
                {"predicted_price": predicted_price[0], "id": prediction_instance.id},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            # Handle any errors that occur during prediction or saving to the database
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BostonHousingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BostonHousing.objects.all()
    serializer_class = BostonHousingSerializer
