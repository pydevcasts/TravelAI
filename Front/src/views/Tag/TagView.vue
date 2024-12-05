<template>
    <DefaultLayout>
        <BreadcrumbDefault :pageTitle="pageTitle" />
        <div class="grid grid-cols-1 gap-9 sm:grid-cols-0">
            <div class="flex flex-col gap-9">
                <DefaultCard cardTitle="Create Tag">
                    <form @submit="submit">
                        <div class="p-6.5">
                            <div class="mb-4.5 ml-3 flex flex-col gap-6 xl:flex-row">
                                <InputGroup
                                    required="true"
                                    label="Tag"
                                    v-model="tag"
                                    type="text"
                                    placeholder="Enter tag name"
                                    customClasses="w-full xl:w-1/2"
                                />
                            </div>
                            <div class="mb-4.5 ml-3 flex flex-col gap-6 xl:flex-row">
                                <label class="inline-flex items-center cursor-pointer">
                                    <span class="m-3 text-sm font-medium text-gray-900 dark:text-gray-300">Status Mode</span>
                                    <input type="checkbox" v-model="isDraft" class="sr-only peer" />
                                    <div class="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-blue-600"></div>
                                </label>
                            </div>
                            <button 
                                type="submit"
                                class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90"
                                :disabled="loading"
                            >
                                <span v-if="loading">Loading...</span>
                                <span v-else>Submit</span>
                            </button>
                            <div v-if="errorMessage" class="error-message text-red-600 mt-4">{{ errorMessage }}</div>
                        </div>
                    </form>
                </DefaultCard>
            </div>
        </div>
    </DefaultLayout>
</template>

<script setup lang="ts">
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue';
import DefaultCard from '@/components/Forms/DefaultCard.vue';
import InputGroup from '@/components/Forms/InputGroup.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import { useToast } from "vue-toastification";
import { ref,computed } from 'vue';
import instance from '@/axios';

const toast = useToast();
const pageTitle = ref<string>('Tag');
const tag = ref<string | null>(null);
const isDraft = ref<boolean>(false); // متغیر برای وضعیت چک باکس
const loading = ref<boolean>(false);
const errorMessage = ref<string | null>(null);

// محاسبه وضعیت بر اساس چک باکس
const status = computed(() => isDraft.value ? 'true' : 'false');

// Validate inputs before making the API call
const validateInputs = (): boolean => {
    if (!tag.value) {
        errorMessage.value = "Tag is required.";
        return false;
    }
    errorMessage.value = null; // Clear previous error message
    return true;
};

const submit = async (event: Event) => {
    event.preventDefault(); // Prevent default form submission
    if (!validateInputs()) {
        return; // Stop if inputs are not valid
    }
    loading.value = true; // Start loading

    try {
        console.log('Input values:', { tag: tag.value, status: status.value });

        const response = await instance.post('/api/tag/', {
            name: String(tag.value),
            status: status.value, // ارسال وضعیت
        });

        console.log('API Response:', response);

        tag.value = response.data.name || tag.value; // fallback in case name is null
        toast.success("Tag successfully created!", { timeout: 2000 });
        tag.value= ""
    } catch (error) {
        console.error('Error creating tag:', error);
        toast.error("There was a problem!", { timeout: 2000 });
        errorMessage.value = "An error occurred. Please try again.";
    } finally {
        loading.value = false; // Stop loading
    }
};
</script>
<style scoped>
.error-message {
    color:red
}
</style>