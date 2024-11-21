<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <DefaultAuthCard subtitle="Start for free" :title="pageTitle">
      <SignInForm v-if="showSignInForm"  @show="showSignInForm = false"/>
      <ResetPassword v-else  />
    </DefaultAuthCard>
  </div>
</template>


<script setup lang="ts">
import DefaultAuthCard from "@/components/Auths/DefaultAuthCard.vue";
import SignInForm from "@/components/Auths/SignInForm.vue";
import ResetPassword from "@/components/Auths/ResetPassword.vue";
import {computed, ref} from "vue";

let showSignInForm = ref(true)

const pageTitle = computed(() => {
  return showSignInForm.value ? 'Sign In' : 'Forget Password'
})

</script>
