<template>
  <v-app>
    <default-bar @show-login-dialog="showLoginDialog"/>
    <default-view />
  </v-app>

  <v-dialog :model-value="isShowLoginModal"
    @click:outside="closeLoginDialog"
    width="auto" min-width="600" 
    transition="dialog-bottom-transition"
  >
    <v-card>
      <v-form ref="login_form" @submit="onLogin" >
        <v-card-title>
          {{ $t('dialog.login') }}
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
              >
                <v-text-field type="email"
                  label="email*"
                  :rules="rule_email_req"
                  v-model="login_data.email"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                cols="12"
              >
                <v-text-field type="password"
                  label="password*"
                  :rules="rule_password_req"
                  v-model="login_data.password"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="closeLoginDialog">{{ $t('dialog.close') }}</v-btn>
          <v-btn color="success" type="submit">{{ $t('dialog.login') }}</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>

  <v-snackbar :model-value="isShowSnackbar">
    {{ getSnackbarBody }}
    <template v-slot:actions>
      <v-btn
        color="pink"
        variant="text"
        @click="hideSnackbar"
      >
        Close
      </v-btn>
    </template>
  </v-snackbar>

  <v-overlay :model-value="isShowLoadingModal" class="text-center" :persistent="true">
    <div class="text-center" id="loading-wrap">
      <v-progress-circular  :size="200" :width="15"
        indeterminate
        color="purple"
      ></v-progress-circular>
    </div>
  </v-overlay>
</template>

<script setup>
  import {reactive, ref, computed, watch} from "vue";
  import { useRouter } from 'vue-router';
  import {useStore} from 'vuex';
  import DefaultBar from './AppBar.vue';
  import DefaultView from './View.vue';
  import {i18n} from '@/plugins/i18n';
  import {auth} from '@/api/service/auth'

  let $router = useRouter();
  const store = useStore();
  const getSnackbarBody = computed(() => {
    return store.getters.getSnackbarBody;
  });
  const isShowSnackbar = computed(() => {
    return store.getters.isSnackbarShow;
  });
  const isShowLoginModal = computed(() => {
    return store.getters.isLoginDialogShow;
  });
  const isShowLoadingModal = computed(() => {
    return store.getters.isShowLoadingModal;
  });


  const login_form = ref(null);
  let login_data = reactive({email: "", password: ""});

  let dialog = reactive({login: false});
  let rule_email_req = [
    value => {
      if (!value) return i18n.global.t("login_form.email_req");
      let is_email = value.match(
        /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      )
      if(!is_email)
        return i18n.global.t("login_form.email_format_req");
      return true;
    },
  ];
  let rule_password_req = [
    value => {
      if (value) return true
      return i18n.global.t("login_form.password_req")
    },
  ];

  function showLoginDialog(){
    console.log("showLoginDialog");
    store.commit('changeVisibleLoginDialog', true);
  }
  function closeLoginDialog(){
    console.log("closeLoginDialog");
    store.commit('changeVisibleLoginDialog', false);
  }

  function onLogin(e){
    e.preventDefault();
    
    let validate = login_form.value.validate();
    if(validate.valid == false){
      return;
    }
    auth.login(login_data.email, login_data.password).then(
      function(response){
        closeLoginDialog();
        let msg = i18n.global.t("login_form.success");
        store.commit('setLoginEmail', login_data.email);
        store.commit('changeLogin', true);
        store.commit('showSnackbar', msg, 3000);
        let access_token = response.data.access_token;
        auth.setLoginToken(access_token);
        $router.go(0)
      }
    ).catch(
      function(error){
        let response = error.response.data;
        if("detail" in response == false){
          return;
        }
        let detail = response.detail;
        let msg = i18n.global.t(detail);;
        store.commit('showSnackbar', msg, -1);
      }
    );
  }

  function hideSnackbar(){
    store.commit('hideSnackbar');
  }
</script>

<style>
#loading-wrap{
  position: absolute;
  left: calc(50vw - 100px);
  top: calc(50vh - 150px);
}
</style>