import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    common: {
      title: "Startup ERP",
    },
    menu: {
      user: "account",
      person: "person",
      deal: "deal",
      product: "product",
      accounting: "accounting",
    },
    dialog: {
      login: 'Login',
      close: 'Close',
    },
    login_form: {
      email_req: 'Email is required.',
      email_format_req: 'The email format is not correct.',
      password_req: 'Password is required.',
      success: 'log-in succeed',
      id_or_pw_incorrect: 'ID or password is incorrect.',
    },
  },
  ko: {
    common: {
      title: "스타트업 ERP",
    },
    menu: {
      user: "계정",
      person: "사용자",
      deal: "거래",
      product: "재화",
      accounting: "회계",
    },
    dialog: {
      login: '로그인',
      close: '닫기',
    },
    login_form: {
      email_req: '이메일은 필수 입니다.',
      email_format_req: '이메일 형식에 맞지 않습니다.',
      password_req: '패스워드는 필수 입니다.',
      success: '로그인 성공',
      id_or_pw_incorrect: '아이디나 패스워드가 올바르지 않습니다.',
    },
  }
};

export const i18n = new createI18n({
  legacy: false,
  locale: 'ko', // set locale
  messages
});
