<template>
  <v-main class="main">
    <router-view :key="$route.fullPath" />
  </v-main>
</template>

<script setup>
  //
</script>

<style scoped>
.main{
  margin: 20px 20px;
}

.data-list-table table thead tr th{
  background-color: black;
}



</style>