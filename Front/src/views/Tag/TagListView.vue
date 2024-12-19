<template>
    <DefaultLayout>
        <BreadcrumbDefault :pageTitle="pageTitle" />
        <div class="grid grid-cols-1 gap-9 sm:grid-cols-0">
            <div class="flex flex-col gap-9">
          <TableTag></TableTag>
            </div>
        </div>
    </DefaultLayout>
</template>

<script setup lang="ts">
import TableTag from '@/components/Tables/TableTag.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';


</script>
