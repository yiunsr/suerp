import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    common: {
      title: "Startup ERP",
      login_required: "Login required.",
    },
    model: {
      user: "user",
    },
    menu: {
      user: "user",
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
    ui_table: {
      search: "search",
      no_data: "No data available",
      per_page: "Items per page"
    },
    page_user_list: {
      title: "User List",
      email: "email",
      last_name: "last name",
      first_name: "rist name",
    },
  },
  ko: {
    common: {
      title: "스타트업 ERP",
      login_required: "로그인 필요합니다.",
    },
    model: {
      user: "유저",
    },
    menu: {
      user: "유저",
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
    ui_table: {
      search: "검색",
      no_data: "데이터 없음",
      per_page: "페이지당 아이템수"
    },
    page_user_list: {
      title: "유저 리스트",
      email: "이메일",
      last_name: "성",
      first_name: "이름",
    },
  }
};

export const i18n = new createI18n({
  legacy: false,
  locale: 'ko', // set locale
  messages
});
