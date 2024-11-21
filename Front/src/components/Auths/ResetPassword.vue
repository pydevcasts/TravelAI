<script lang="ts" setup>
import InputGroup from "@/components/Auths/InputGroup.vue";
import { ref} from 'vue';
import instance from '@/axios';
import {useToast} from "vue-toastification";

const toast = useToast();
const email = ref('');
const error = ref('');


const onResetPassword = async () => {
  try {
    const response = await instance.post('/rest-auth/password/reset/', {
      email: email.value,
    }).then((res)=>{
      console.log(res)
    });
    toast.success("An Email Sent To You, Please Check Your Email", {timeout: 2000});
console.log(response)
  } catch (err) {
    handleLoginError(err);
  }
};

const handleLoginError = (err: any) => {
  if (err.response) {
    console.error('Response data:', err.response.data);
    toast.error(`failed. : ${err.response.data.message || 'Unauthorized'}`, {timeout: 2000});
  } else {
    error.value = 'failed. Please try again.';
  }
};

</script>
<template>
  <form @submit.prevent="onResetPassword">
    <InputGroup label="Email" type="email" placeholder="Enter your email" v-model="email" />

    <div class="mb-5 mt-6">
      <input
          class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
          type="submit"
          value="Confirm"/>
    </div>
  </form>
</template>

<style lang="scss" scoped>

</style>
