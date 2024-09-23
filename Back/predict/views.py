import joblib
import numpy as np
from .models import BostonHousing  # Import your model
from rest_framework import generics
from rest_framework.response import Response
from .serializers import BostonHousingSerializer  # Import your serializer
from rest_framework.permissions import IsAuthenticated 


# Load your model (make sure the path is correct)
model = joblib.load('boston_housing_model.pkl')

class BostonHousingListCreateView(generics.ListCreateAPIView):
    queryset = BostonHousing.objects.all()
    serializer_class = BostonHousingSerializer
    permission_classes = [IsAuthenticated]  # Set permission classes


    def post(self, request, *args, **kwargs):
        crim = request.data.get('crim')
        zn = request.data.get('zn')
        indus = request.data.get('indus')
        chas = request.data.get('chas')
        nox = request.data.get('nox')
        rm = request.data.get('rm')
        age = request.data.get('age')
        dis = request.data.get('dis')
        rad = request.data.get('rad')
        tax = request.data.get('tax')
        ptratio = request.data.get('ptratio')
        b = request.data.get('b')
        lstat = request.data.get('lstat')
        # Prepare input data for prediction
        input_data = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
        # Make prediction
        predicted_price = model.predict(input_data)
        return Response({'predicted_price': predicted_price[0]})
    

class BostonHousingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BostonHousing.objects.all()
    serializer_class = BostonHousingSerializer

