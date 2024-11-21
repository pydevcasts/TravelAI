<script setup lang="ts">
import DefaultAuthCard from "@/components/Auths/DefaultAuthCard.vue";
import { ref } from "vue";
import InputGroup from "@/components/Auths/InputGroup.vue";
import instance from "@/axios";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";

const toast = useToast();
const router = useRouter();
const pageTitle = ref('Reset Password');
const newPassword1 = ref('');
const newPassword2 = ref('');
const error = ref('');

const changePassword = async () => {
  // Check if passwords match
  if (newPassword1.value !== newPassword2.value) {
    toast.error("Passwords do not match.", { timeout: 2000 });
    return;
  }

  try {
    const response = await instance.post('/rest-auth/password/change/', {
      new_password1: newPassword1.value,
      new_password2: newPassword2.value
    });

    console.log(response);
    toast.success("Your Password Changed Successfully.", { timeout: 2000 });
    router.push('/');
  } catch (err) {
    handleLoginError(err);
  }
}

const handleLoginError = (err: any) => {
  if (err.response) {
    console.error('Response data:', err.response.data);
    if (err.response.status === 401) {
      toast.error("Unauthorized: Please log in again.", { timeout: 2000 });
      // Optionally redirect to login page
      router.push('/signin');
    } else {
      toast.error(`Failed: ${err.response.data.message || 'An error occurred'}`, { timeout: 2000 });
    }
  } else {
    error.value = 'Failed. Please try again.';
  }
}
</script>

<template>

  <div class="flex items-center justify-center min-h-screen bg-gray-100">
  <DefaultAuthCard :title="pageTitle" >
    <form @submit.prevent="changePassword">
      <InputGroup v-model="newPassword1" label="New Password" placeholder="Enter your password" type="password">
        <svg
            class="fill-current"
            fill="none"
            height="22"
            viewBox="0 0 22 22"
            width="22"
            xmlns="http://www.w3.org/2000/svg"
        >
          <g opacity="0.5">
            <path
                d="M16.1547 6.80626V5.91251C16.1547 3.16251 14.0922 0.825009 11.4797 0.618759C10.0359 0.481259 8.59219 0.996884 7.52656 1.95938C6.46094 2.92188 5.84219 4.29688 5.84219 5.70626V6.80626C3.84844 7.18438 2.33594 8.93751 2.33594 11.0688V17.2906C2.33594 19.5594 4.19219 21.3813 6.42656 21.3813H15.5016C17.7703 21.3813 19.6266 19.525 19.6266 17.2563V11C19.6609 8.93751 18.1484 7.21876 16.1547 6.80626ZM8.55781 3.09376C9.31406 2.40626 10.3109 2.06251 11.3422 2.16563C13.1641 2.33751 14.6078 3.98751 14.6078 5.91251V6.70313H7.38906V5.67188C7.38906 4.70938 7.80156 3.78126 8.55781 3.09376ZM18.1141 17.2906C18.1141 18.7 16.9453 19.8688 15.5359 19.8688H6.46094C5.05156 19.8688 3.91719 18.7344 3.91719 17.325V11.0688C3.91719 9.52189 5.15469 8.28438 6.70156 8.28438H15.2953C16.8422 8.28438 18.1141 9.52188 18.1141 11V17.2906Z"
                fill=""
            />
            <path
                d="M10.9977 11.8594C10.5852 11.8594 10.207 12.2031 10.207 12.65V16.2594C10.207 16.6719 10.5508 17.05 10.9977 17.05C11.4102 17.05 11.7883 16.7063 11.7883 16.2594V12.6156C11.7883 12.2031 11.4102 11.8594 10.9977 11.8594Z"
                fill=""
            />
          </g>
        </svg>
      </InputGroup>

      <InputGroup v-model="newPassword2" label="Re-type Password" placeholder="Re-enter your password"
                  type="password">
        <svg
            class="fill-current"
            fill="none"
            height="22"
            viewBox="0 0 22 22"
            width="22"
            xmlns="http://www.w3.org/2000/svg"
        >
          <g opacity="0.5">
            <path
                d="M16.1547 6.80626V5.91251C16.1547 3.16251 14.0922 0.825009 11.4797 0.618759C10.0359 0.481259 8.59219 0.996884 7.52656 1.95938C6.46094 2.92188 5.84219 4.29688 5.84219 5.70626V6.80626C3.84844 7.18438 2.33594 8.93751 2.33594 11.0688V17.2906C2.33594 19.5594 4.19219 21.3813 6.42656 21.3813H15.5016C17.7703 21.3813 19.6266 19.525 19.6266 17.2563V11C19.6609 8.93751 18.1484 7.21876 16.1547 6.80626ZM8.55781 3.09376C9.31406 2.40626 10.3109 2.06251 11.3422 2.16563C13.1641 2.33751 14.6078 3.98751 14.6078 5.91251V6.70313H7.38906V5.67188C7.38906 4.70938 7.80156 3.78126 8.55781 3.09376ZM18.1141 17.2906C18.1141 18.7 16.9453 19.8688 15.5359 19.8688H6.46094C5.05156 19.8688 3.91719 18.7344 3.91719 17.325V11.0688C3.91719 9.52189 5.15469 8.28438 6.70156 8.28438H15.2953C16.8422 8.28438 18.1141 9.52188 18.1141 11V17.2906Z"
                fill=""
            />
            <path
                d="M10.9977 11.8594C10.5852 11.8594 10.207 12.2031 10.207 12.65V16.2594C10.207 16.6719 10.5508 17.05 10.9977 17.05C11.4102 17.05 11.7883 16.7063 11.7883 16.2594V12.6156C11.7883 12.2031 11.4102 11.8594 10.9977 11.8594Z"
                fill=""
            />
          </g>
        </svg>
      </InputGroup>

      <div class="mb-5 mt-6">
        <input type="submit" value="Confirm" class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90" />
      </div>
    </form>
  </DefaultAuthCard>
  </div>
</template>

<style scoped lang="scss">

</style>