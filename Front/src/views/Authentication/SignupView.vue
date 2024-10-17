<script lang="ts" setup>
import DefaultAuthCard from '@/components/Auths/DefaultAuthCard.vue'
import SignUpForm from "@/components/Auths/SignUpForm.vue";
import VerifyMailForm from "@/components/Auths/VerifyMailForm.vue";
import {ref} from 'vue'

const pageTitle = ref('Sign Up')
let email = ref('')
let showSignUpForm = ref(true)

const setMail = (payload: string) => {
  email.value = payload
  showSignUpForm.value = false
}
</script>

<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">

    <DefaultAuthCard :title="pageTitle" subtitle="Start for free">
      <SignUpForm v-if="showSignUpForm" @setMail="setMail"/>
      <VerifyMailForm v-else :email="email"/>
    </DefaultAuthCard>

  </div>
</template>
