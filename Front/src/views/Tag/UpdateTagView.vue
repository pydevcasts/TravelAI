<template>
    <DefaultLayout>
        <BreadcrumbDefault :pageTitle="pageTitle" />
        <div class="grid grid-cols-1 gap-9 sm:grid-cols-0">
            <div class="flex flex-col gap-9">
                <DefaultCard cardTitle="Update Tag">
                    <form @submit.prevent="updateTag">
                        <div class="p-6.5">
                            <div class="mb-4.5 ml-3 flex flex-col gap-6 xl:flex-row">
                                <InputGroup
                                    required="true"
                                    label="Tag"
                                    v-model="tagName"
                                    type="text"
                                    placeholder="Enter tag name"
                                    customClasses="w-full xl:w-1/2"
                                />
                            </div>
                            <div class="mb-4.5 ml-3 flex flex-col gap-6 xl:flex-row">
                                <label class="inline-flex items-center cursor-pointer">
                                    <span class="m-3 text-sm font-medium text-gray-900 dark:text-gray-300">Status Mode</span>
                                    <input type="checkbox" v-model="tagStatus" class="sr-only peer" />
                                    <div class="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-blue-600"></div>
                                </label>
                            </div>
                            <button
                                type="submit"
                                class="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90"
                                :disabled="loading"
                            >
                                <span v-if="loading">Loading...</span>
                                <span v-else>Update</span>
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
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import instance from '@/axios';
import router from '@/router';

const toast = useToast();
const route = useRoute();
const pageTitle = ref<string>('Update Tag');
const tagName = ref<string>('');
const tagStatus = ref<boolean>(false);
const loading = ref<boolean>(false);
const errorMessage = ref<string | null>(null);
const tagId = ref<number>(Number(route.params.id));

onMounted(async () => {
    try {
        const response = await instance.get(`/api/tag/${tagId.value}/`);
        tagName.value = response.data.name;
        tagStatus.value = response.data.status;
    } catch (error) {
        console.error('Error fetching tag:', error);
        errorMessage.value = "Failed to fetch tag information.";
    }
});

const updateTag = async () => {
    try {
        loading.value = true;
        await instance.put(`/api/tag/${tagId.value}/`, {
            name: tagName.value,
            status: tagStatus.value,
        });
        toast.success("Tag updated successfully!", { timeout: 2000 });
        router.push('/tags/')
        // Redirect the user back to the list page or show a success message
    } catch (error) {
        console.error('Error updating tag:', error);
        toast.error("Failed to update tag.", { timeout: 2000 });
        errorMessage.value = "An error occurred. Please try again.";
    } finally {
        loading.value = false;
    }
};
</script>

<style scoped>
.error-message {
    color:red
}
</style>
