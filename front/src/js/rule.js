import {i18n} from '@/plugins/i18n';
let t=i18n.global.t;

const rule = {
  req: (value) => {
    if (value) return true
    return t('rule.required');
  },
  req_debugger: (value) => {
    debugger
    if (value) return true
    return t('rule.required');
  },
  email: (value) => {
    // https://stackoverflow.com/a/46181
    let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let valid = re.test(value);
    if (valid) return true
    return t('rule.email');
  },
}

export {rule}