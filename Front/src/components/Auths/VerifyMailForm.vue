<script lang="ts" setup>
import InputGroup from "@/components/Auths/InputGroup.vue";
import {defineProps, onMounted, ref} from 'vue';
import instance from '@/axios';
import {useToast} from "vue-toastification";
import {useRouter} from "vue-router";

const toast = useToast();
const router = useRouter();
const props = defineProps(['email'])
const key = ref('');
let showCounter = ref(true);
let counter = ref(0)
const error = ref('');


const onVerify = async () => {
  try {
    await instance.post('/rest-auth/registration/verify-email/', {
      key: key.value,
    });
    toast.success("Your Email Verified.", {timeout: 2000});
    router.push('/signin');

  } catch (err) {
    handleLoginError(err);
  }
};

const onResendKey = async () => {
  try {
    await instance.post('/rest-auth/registration/resend-email/', {
      email: props.email,
    });
    setCounter()
    showCounter.value = true
    toast.success("We Sent you Another Code.", {timeout: 2000});
  } catch (err) {
    handleLoginError(err);
  }
}

const handleLoginError = (err: any) => {
  if (err.response) {
    console.error('Response data:', err.response.data);
    toast.error(`Your email verifying failed. : ${err.response.data.message || 'Unauthorized'}`, {timeout: 2000});
  } else {
    error.value = 'Your email verifying failed. Please try again.';
  }
};

const setCounter = (duration = 60) => {
  counter.value = duration

  const loop = setInterval(() => {
    if (counter.value > 0) {
      counter.value--
    } else {
      showCounter.value = false
      clearInterval(loop);
    }
  }, 1000)
}

const setTwoDigit = (number: number) => {
  if (number < 10) return `0${number}`
  else return number
}

onMounted(() => {
  setCounter()
})
</script>
<template>
  <form @submit.prevent="onVerify">
    <InputGroup v-model="key" class="mt-6" label="Enter The Code we have Sent To Your Email."
                type="number"/>

    <div class="mb-5 mt-6">
      <input
          class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
          type="submit"
          value="Verify"/>
    </div>


    <div class="mt-6 text-center">
      <p v-show="showCounter && counter > 0" class="font-medium text-opacity-60">

        Resend Code after 00:{{ setTwoDigit(counter) }}
      </p>
      <p v-show="!showCounter && counter === 0" class="font-medium">

        Didn’t receive a code?
        <button class="text-primary" @click.prevent="onResendKey">Resend</button>
      </p>
    </div>
  </form>
</template>

<style lang="scss" scoped>

</style>