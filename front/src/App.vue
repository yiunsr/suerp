<template>
  <Default></Default>
</template>

<script setup>
import Default from './layouts/default/Default.vue';

  //
</script>

<style>
table.header-table{
  width: 100%;
}
table.header-table col:first-child{
  width: calc(100% - 25px);
}
table.header-table col:nth-child(2){
  width: 25px;
}
table.header-table col:last-child{
  width: 25px;
}
table.header-table, table.header-table td {
  border: 1px solid #616161;
  border-collapse: collapse;
}
table.header-table, table.header-table td:nth-child(2) {
  border: 1px solid #616161;
  border-collapse: collapse;
}
table.header-table button{
  min-width: 38px;
  height: 32px !important;
}

table.header-table tbody tr > td > div{
  max-height: 0px;
  overflow: hidden;
}

table.header-table tbody.show tr > td > div{
  max-height: 100%;
  overflow: inherit;
}

.data-list-table th, .data-list-table td{
  padding: 1px 4px !important;
}
.data-list-table thead tr th{
  background-color: #212121 !important;
  color: #F5F5F5 !important;
}

.data-list-table tbody tr:nth-child(odd) td{
  background-color: #F5F5F5 !important;
}

/******** .table-filter start ********/
.data-list-table .table-filter .v-field input{
  font-size: 13.5px;
}

/* <v-text-fiel> */
.data-list-table .table-filter .v-input.v-text-field .v-field__field input{
  padding: 3px 4px !important;
  
}
/* </v-text-fiel> */

/* <v-text-fiel> */
.data-list-table .table-filter .v-input.v-select .v-field__input{
  padding: 3px 4px !important;
  
}
/* </v-text-fiel> */

/******** .table-filter end ********/
</style>