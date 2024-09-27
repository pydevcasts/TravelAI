<script setup lang="ts">
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultCard from '@/components/Forms/DefaultCard.vue'
import InputGroup from '@/components/Forms/InputGroup.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import { useToast } from "vue-toastification";
import { ref } from 'vue'
import axios from 'axios'
const toast = useToast();
const pageTitle = ref('Predict House');
const crim = ref<number | null>(null);
const zn = ref<number | null>(null);
const indus = ref<number | null>(null);
const chas = ref<number | null>(null);
const nox = ref<number | null>(null);
const rm = ref<number | null>(null);
const age = ref<number | null>(null);
const dis = ref<number | null>(null);
const rad = ref<number | null>(null);
const tax = ref<number | null>(null);
const ptratio = ref<number | null>(null);
const b = ref<number | null>(null);
const lstat = ref<number | null>(null);
const predictedPrice = ref<number | null>(null);
const loading = ref<boolean>(false);
const errorMessage = ref<string | null>(null);

// Validate inputs before making the API call
const validateInputs = () => {
  if (crim.value === null || zn.value === null || indus.value === null || chas.value === null ||
      nox.value === null || rm.value === null || age.value === null || dis.value === null ||
      rad.value === null || tax.value === null || ptratio.value === null || b.value === null ||
      lstat.value === null) {
    errorMessage.value = "All fields are required.";
    return false;
  }
  errorMessage.value = null; // Clear previous error message
  return true;
};

const predict = async (event: Event) => {
  event.preventDefault(); // Prevent default form submission
  
  if (!validateInputs()) {
    return; // Stop if inputs are not valid
  }

  loading.value = true; // Start loading

  try {
    console.log('Input values:', {
      crim: crim.value,
      zn: zn.value,
      indus: indus.value,
      chas: chas.value,
      nox: nox.value,
      rm: rm.value,
      age: age.value,
      dis: dis.value,
      rad: rad.value,
      tax: tax.value,
      ptratio: ptratio.value,
      b: b.value,
      lstat: lstat.value,
    });
    
    const token = localStorage.getItem('access');
    const response = await axios.post('http://localhost:8000/api/predict/', {
      crim: Number(crim.value),
      zn: Number(zn.value),
      indus: Number(indus.value),
      chas: Number(chas.value),
      nox: Number(nox.value),
      rm: Number(rm.value),
      age: Number(age.value),
      dis: Number(dis.value),
      rad: Number(rad.value),
      tax: Number(tax.value),
      ptratio: Number(ptratio.value),
      b: Number(b.value),
      lstat: Number(lstat.value),
    },{
  
      headers: {
        'Authorization': `Bearer ${token}`, // Include the token in the headers
      }
  
    });

    predictedPrice.value = response.data.predicted_price;
    toast.success("Price is predicted successful!", { timeout: 2000 });
  } catch (error) {
    toast.error("There are problem!", { timeout: 2000 });
    console.error('Error predicting price:', error);
    errorMessage.value = "An error occurred while predicting the price. Please try again.";
  } finally {
    loading.value = false; // Stop loading
  }
};
</script>

<template>
  <DefaultLayout>
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <div class="grid grid-cols-1 gap-9 sm:grid-cols-0">
      <div class="flex flex-col gap-9">
        <DefaultCard cardTitle="Predict House Price">
          <form @submit="predict">
            <div class="p-6.5">
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup label="Crime Rate (crim)" v-model="crim" type="number" placeholder="Enter crime rate" customClasses="w-full xl:w-1/2" />
                <InputGroup label="Residential Land Zoned (zn)" v-model="zn" type="number" placeholder="Enter residential land zoned" customClasses="w-full xl:w-1/2" />
              </div>
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup label="Non-retail Business Acres (indus)" v-model="indus" type="number" placeholder="Enter non-retail business acres" customClasses="w-full xl:w-1/2" />
                <InputGroup label="Charles River Dummy Variable (chas)" v-model="chas" type="number" placeholder="Enter Charles River dummy variable" customClasses="w-full xl:w-1/2" />
              </div>
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup label="Nitric Oxides Concentration (nox)" v-model="nox" type="number" placeholder="Enter nitric oxides concentration" customClasses="w-full xl:w-1/2" />
                <InputGroup label="Average Number of Rooms (rm)" v-model="rm" type="number" placeholder="Enter average number of rooms" customClasses="w-full xl:w-1/2" />
              </div>
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup label="Proportion of Owner-occupied Units (age)" v-model="age" type="number" placeholder="Enter proportion of owner-occupied units" customClasses="w-full xl:w-1/2" />
                <InputGroup label="Weighted Distances to Employment Centers (dis)" v-model="dis" type="number" placeholder="Enter weighted distances to employment centers" customClasses="w-full xl:w-1/2" />
              </div>
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup label="Index of Accessibility to Radial Highways (rad)" v-model="rad" type="number" placeholder="Enter index of accessibility to radial highways" customClasses="w-full xl:w-1/2" />
                <InputGroup label="Full-value Property Tax Rate (tax)" v-model="tax" type="number" placeholder="Enter full-value property tax rate" customClasses="w-full xl:w-1/2" />
              </div>
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup label="Pupil-teacher Ratio (ptratio)" v-model="ptratio" type="number" placeholder="Enter pupil-teacher ratio" customClasses="w-full xl:w-1/2" />
                <InputGroup label="Value of B (b)" v-model="b" type="number" placeholder="Enter the value of B" customClasses="w-full xl:w-1/2" />
              </div>
              <div class="mb-4.5 flex flex-col gap-6 xl:flex-row">
                <InputGroup label="Percentage of Lower Status of the Population (lstat)" v-model="lstat" type="number" placeholder="Enter percentage of lower status of the population" customClasses="w-full xl:w-1/2" />
              </div>
              <button type="submit" class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90" :disabled="loading">
                <span v-if="loading">Loading...</span>
                <span v-else>Predict Price</span>
              </button>
              <div v-if="predictedPrice !== null" class="mt-4">
                <h1>Predicted Price is: {{ predictedPrice }}</h1>
              </div>
              <div v-if="errorMessage" class="text-red-500 mt-4">{{ errorMessage }}</div>
            </div>
          </form>
        </DefaultCard>
      </div>
    </div>
  </DefaultLayout>
</template>