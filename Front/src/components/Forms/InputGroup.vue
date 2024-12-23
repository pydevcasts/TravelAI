<script lang="ts">
import { defineComponent, ref, watch } from 'vue';

export default defineComponent({
  props: {
    modelValue: {
      type: [String, Number],
      default: ''
    },
    label: {
      type: String,
      required: true // Make label required
    },
    type: {
      type: String,
      default: 'text' // Default input type is text
    },
    placeholder: String,
    customClasses: String,
    required: {
      type: Boolean,
      default: false
    },
    errorMessage: {
      type: String,
      default: ''
    }
  },
  emits: ['update:modelValue'], // Declare the emitted event
  setup(props, { emit }) {
    const inputValue = ref(props.modelValue); // Create a local ref for the input value
    const showPassword = ref(false); // For toggling password visibility

    // Watch for changes in modelValue prop to update local inputValue
    watch(() => props.modelValue, (newValue) => {
      inputValue.value = newValue;
    });

    // Emit the value when the input changes
    const handleInput = (event: Event) => {
      const value = (event.target as HTMLInputElement).value; // Get the input value
      inputValue.value = value; // Update local ref
      emit('update:modelValue', value); // Emit the updated value
    };

    // Toggle password visibility
    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value;
    };

    return { inputValue, handleInput, showPassword, togglePasswordVisibility };
  }
});
</script>

<template>
  <div :class="customClasses">
    <label class="mb-2.5 block text-black dark:text-white">
      {{ label }}
      <span v-if="required" class="text-meta-1">*</span>
    </label>
    <div class="relative">
      <input
        :type="showPassword && type === 'password' ? 'text' : type"
        :placeholder="placeholder"
        :value="inputValue"
        @input="handleInput"
        class="w-full rounded border-[1.5px] text-black border-stroke bg-transparent py-3 px-5 font-normal outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:text-white dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary"
      />
      <span v-if="type === 'password'" @click="togglePasswordVisibility" class="absolute right-3 top-3 cursor-pointer">
        {{ showPassword ? 'Hide' : 'Show' }}
      </span>
    </div>
    <p v-if="errorMessage" class="text-red-500 text-sm mt-1">{{ errorMessage }}</p> <!-- Error message -->
  </div>
</template>
