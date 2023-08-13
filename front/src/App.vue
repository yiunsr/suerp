<template>
  <Default></Default>
</template>

<script setup>
import Default from './layouts/default/Default.vue';

  //
</script>

<style>
table.search-table{
  width: 100%;
}
table.search-table col:first-child{
  width: calc(100% - 25px);
}
table.search-table col:nth-child(2){
  width: 25px;
}
table.search-table col:last-child{
  width: 25px;
}
table.search-table, table.search-table td {
  border: 1px solid #616161;
  border-collapse: collapse;
}
table.search-table, table.search-table td:nth-child(2) {
  border: 1px solid #616161;
  border-collapse: collapse;
}
table.search-table button{
  min-width: 38px;
  height: 32px !important;
}

table.search-table tbody tr > td > div{
  max-height: 0px;
  overflow: hidden;
}

table.search-table tbody.show tr > td > div{
  max-height: 100%;
  overflow: inherit;
}

.data-list-table thead tr th{
  background-color: #212121 !important;
  color: #F5F5F5 !important;
}

.data-list-table tbody tr:nth-child(odd) td{
  background-color: #F5F5F5 !important;
}
</style>