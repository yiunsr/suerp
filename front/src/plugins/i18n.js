import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    common: {
      title: "Startup ERP",
    },
    dialog: {
      login: 'Login',
    }
  },
  ko: {
    common: {
      title: "스타트업 ERP",
    },
    dialog: {
      login: '로그인',
    }
  }
};

export const i18n = new createI18n({
  legacy: false,
  locale: 'ko', // set locale
  messages
});
