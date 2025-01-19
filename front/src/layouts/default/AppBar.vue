<template>
  <div>
    <v-app-bar density='compact' height="56">
      <v-app-bar-title>
        <!-- <v-icon icon="mdi-circle-slice-4" />  -->
        {{ $t('common.title') }}
      </v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn icon href="https://vuetifyjs.com/en/" target="_blank">
        <v-icon>mdi-help</v-icon>
      </v-btn>

      <v-btn icon @click="$emit('show-login-dialog')" v-show="isLogin == false">
        <v-icon>mdi-login</v-icon>
      </v-btn>

      <span v-show="isLogin == true">
        <v-menu >
          <template v-slot:activator="{ props }">
            <v-btn icon="mdi-account-circle"  v-bind="props"></v-btn>
          </template>
          <v-list>
            <v-list-item @click="logout">
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </span>

      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn icon="mdi-translate"  v-bind="props"></v-btn>
        </template>
        <v-list expand-on-hover rail>
          <v-list-item  @click="changeLang('en')">
            <v-list-item-title>English</v-list-item-title>
          </v-list-item>
          <v-list-item  @click="changeLang('ko')">
            <v-list-item-title>한국어</v-list-item-title>
          </v-list-item>
          <v-list-item  @click="changeLang('key')">
            <v-list-item-title>key</v-list-item-title>
          </v-list-item>
          </v-list>
        </v-menu>
    </v-app-bar>

    <v-navigation-drawer v-model="nav.drawer" :rail="nav.rail"
      permanent @click="nav.rail = false"
    >
      <v-list-item
        prepend-icon="mdi-menu" 
        icon 
      >
        <v-list-item-subtitle v-show="isLogin">{{ loginEmail }}</v-list-item-subtitle>
        <template v-slot:append>
          <v-btn
            variant="text"
            icon="mdi-chevron-left"
            @click.stop="nav.rail = !nav.rail"
          ></v-btn>
        </template>
      </v-list-item>
      <v-list density="compact" nav>
        <v-list-item prepend-icon="mdi-account-key"
          :title="i18n.global.t('menu.user')" 
          value="user" to="/user">
        </v-list-item>
        <v-list-item prepend-icon="mdi-clipboard-account"
          :title="i18n.global.t('menu.person')" 
          value="person" to="/person">
        </v-list-item>
        <v-list-item prepend-icon="mdi-gift" :title="i18n.global.t('menu.product')" value="product"></v-list-item>
        <v-list-item prepend-icon="mdi-handshake-outline" :title="i18n.global.t('menu.deal')" value="deal"></v-list-item>
        <v-list-item prepend-icon="mdi-calculator" :title="i18n.global.t('menu.accounting')" value="accounting"></v-list-item>
        <v-list-item prepend-icon="mdi-view-column-outline"
          :title="i18n.global.t('menu.col_meta')" 
          value="col_meta" to="/col_meta">
        </v-list-item>
        <v-list-item prepend-icon="mdi-shape"
          :title="i18n.global.t('menu.cate_meta')" 
          value="cate_meta" to="/cate_meta">
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script setup>
  import { i18n } from '@/plugins/i18n';
  import {useStore} from 'vuex';
  import {computed, reactive} from "vue";
  import {auth} from '@/api/service/auth'

  let nav = reactive({
    drawer: true, rail: false,
  });

  const store = useStore();
  function changeLang(newLocale){
    store.commit('changeLang', newLocale);
    i18n.global.locale.value = newLocale;
  }
  function logout(){
    store.commit('setLoginEmail', '');
    store.commit('changeLogin', false);
    // sessionStorage.removeItem("access_token");
    auth.removeLoginToken();
  }

  const emit = defineEmits([
    'show-login-dialog'
  ]);

  const isLogin = computed(() => {
    return store.getters.isLogin;
  });
  const loginEmail = computed(() => {
    return store.getters.getLoginEmail;
  });
</script>
