<script setup lang="ts">
import instance from '@/axios';
import { useUserStore } from '@/stores/userStore';
import { ref, onMounted } from 'vue';
import { useToast } from "vue-toastification";

// Sample user data
const users = ref();
const userStore = useUserStore();
const toast = useToast();
const editUser = (userId: number) => {
  console.log(`Edit user with ID: ${userId}`);
};
const deleteUser = async (userId: number) => {
  try {
    console.log(`Delete user with ID: ${userId}`);
    
    // Make the DELETE request to delete the user
    const response = await instance.delete(`/api/users/${userId}/`);
    
    if (response.status === 204) { // Check if the deletion was successful
      console.log(`User with ID: ${userId} deleted successfully.`);
      // Clear user state in Pinia store
      userStore.clearUser();
      users.value = users.value.filter(user => user.pk !== userId);
      toast.success("User deleted successful!", { timeout: 2000 });
    } else {
      console.error(`Failed to delete user: ${response.data}`);
    }
  } catch (error) {
    toast.error("There are problem!", { timeout: 2000 });
    console.error('Error deleting user:', error);

  }
};

const fetchUsers = async () => {
  const response = await instance.get('/api/users/');
  users.value = response.data;
  console.log('Fetching users...', response);
  
};

onMounted(() => {
  fetchUsers(); // Fetch users when the component mounts
  
});

</script>
<template>
  <div
    class="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
    <div class="max-w-full overflow-x-auto">
      <table class="w-full table-auto">
        <thead>
          <tr class="bg-gray-2 text-left dark:bg-meta-4">
            <th class="min-w-[220px] py-4 px-4 font-medium text-black dark:text-white xl:pl-11">
              FirstName
            </th>
            <th class="min-w-[220px] py-4 px-4 font-medium text-black dark:text-white xl:pl-11">
              LastName
            </th>
            <th class="min-w-[150px] py-4 px-4 font-medium text-black dark:text-white">
              Email
            </th>
            <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">Status</th>
            <th class="py-4 px-4 font-medium text-black dark:text-white">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in users" :key="user.id">
            <td class="py-5 px-4 pl-9 xl:pl-11">
              <h5 class="font-medium text-black dark:text-white">{{ user.first_name }}</h5>
            </td>
            <td class="py-5 px-4 pl-9 xl:pl-11">
              <h5 class="font-medium text-black dark:text-white">{{ user.last_name }}</h5>
            </td>
            <td class="py-5 px-4">
              <p class="text-black dark:text-white">{{ user.email }}</p>
            </td>
            <td class="py-5 px-4">
              <p class="inline-flex rounded-full bg-opacity-10 py-1 px-3 text-sm font-medium"
              >
                {{ user.status }}
              </p>
            </td>
            <td class="py-5 px-4">
              <div class="flex items-center space-x-3.5">
                <button class="hover:text-primary" @click="editUser(user.id)">
                  <!-- Edit Icon -->
                  <svg class="fill-current" width="18" height="18" viewBox="0 0 18 18" fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                    <path
                      d="M8.99981 14.8219C3.43106 14.8219 0.674805 9.50624 0.562305 9.28124C0.47793 9.11249 0.47793 8.88749 0.562305 8.71874C0.674805 8.49374 3.43106 3.20624 8.99981 3.20624C14.5686 3.20624 17.3248 8.49374 17.4373 8.71874C17.5217 8.88749 17.5217 9.11249 17.4373 9.28124C17.3248 9.50624 14.5686 14.8219 8.99981 14.8219ZM1.85605 8.99999C2.4748 10.0406 4.89356 13.5562 8.99981 13.5562C13.1061 13.5562 15.5248 10.0406 16.1436 8.99999C15.5248 7.95936 13.1061 4.44374 8.99981 4.44374C4.89356 4.44374 2.4748 7.95936 1.85605 8.99999Z"
                      fill="" />
                    <path
                      d="M9 11.3906C7.67812 11.3906 6.60938 10.3219 6.60938 9C6.60938 7.67813 7.67812 6.60938 9 6.60938C10.3219 6.60938 11.3906 7.67813 11.3906 9C11.3906 10.3219 10.3219 11.3906 9 11.3906ZM9 7.875C8.38125 7.875 7.875 8.38125 7.875 9C7.875 9.61875 8.38125 10.125 9 10.125C9.61875 10.125 10.125 9.61875 10.125 9C10.125 8.38125 9.61875 7.875 9 7.875Z"
                      fill="" />
                  </svg>
                </button>

                <button class="hover:text-primary" @click="deleteUser(user.pk)">
                  <!-- Delete Icon -->
                  <svg class="fill-current" width="18" height="18" viewBox="0 0 18 18" fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                    <path
                      d="M13.7535 2.47502H11.5879V1.9969C11.5879 1.15315 10.9129 0.478149 10.0691 0.478149H7.90352C7.05977 0.478149 6.38477 1.15315 6.38477 1.9969V2.47502H4.21914C3.40352 2.47502 2.72852 3.15002 2.72852 3.96565V4.8094C2.72852 5.42815 3.09414 5.9344 3.62852 6.1594L4.07852 15.4688C4.13477 16.6219 5.09102 17.5219 6.24414 17.5219H11.7004C12.8535 17.5219 13.8098 16.6219 13.866 15.4688L14.3441 6.13127C14.8785 5.90627 15.2441 5.3719 15.2441 4.78127V3.93752C15.2441 3.15002 14.5691 2.47502 13.7535 2.47502ZM7.67852 1.9969C7.67852 1.85627 7.79102 1.74377 7.93164 1.74377H10.0973C10.2379 1.74377 10.3504 1.85627 10.3504 1.9969V2.47502H7.70664V1.9969H7.67852ZM4.02227 3.96565C4.02227 3.85315 4.10664 3.74065 4.24727 3.74065H13.7535C13.866 3.74065 13.9785 3.82502 13.9785 3.96565V4.8094C13.9785 4.9219 13.8941 5.0344 13.7535 5.0344H4.24727C4.13477 5.0344 4.02227 4.95002 4.02227 4.8094V3.96565ZM11.7285 16.2563H6.27227C5.79414 16.2563 5.40039 15.8906 5.37227 15.3844L4.95039 6.2719H13.0785L12.6566 15.3844C12.6004 15.8625 12.2066 16.2563 11.7285 16.2563Z"
                      fill="" />
                  </svg>
                </button>

             
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>