import { createI18n } from 'vue-i18n'
import { en_dict, ko_dict } from "@/utils/i18n";

const messages = {
  en: {
    ...en_dict
  },
  ko: {
    ...ko_dict
  }
};

export const i18n = new createI18n({
  legacy: false,
  locale: 'ko', // set locale
  messages
});
