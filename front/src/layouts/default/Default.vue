<template>
  <v-app>
    <default-bar @show-login-dialog="showLoginDialog"/>
    <default-view />
  </v-app>

  <v-dialog
      v-model="dialog.login" width="auto" transition="dialog-bottom-transition"
    >
      <v-card>
        <v-card-title>
          {{ $t('dialog.login') }}
        </v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" block @click="dialog.login = false">Close Dialog</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script setup>
  import {reactive} from "vue";
  import DefaultBar from './AppBar.vue'
  import DefaultView from './View.vue'

  let dialog = reactive({login: false});

  function showLoginDialog(){
    dialog.login = true;
  }
</script>
