<script setup lang="ts">
import { ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import TableUser from '@/components/Tables/TableUser.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const pageTitle = ref('Tables')
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <div class="flex flex-col gap-10">

      <TableUser />
    </div>
  </DefaultLayout>
</template>
