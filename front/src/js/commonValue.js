import {i18n} from '@/plugins/i18n';

function prepare(prefix, dict){
  let items = [];
  for(const key in dict){
    let value = dict[key];
    items.push({title: i18n.global.t(prefix + value) , value: key})
  }
  return items;
}

const _UserStatusDict = {
  "A": "available",
  "S": "system",
  "D": "deleted",
  "L": "leave",
  "U": "unusable",
  "H": "hidden",
}
const UserStatusItems = prepare("common_const.status.", _UserStatusDict);

const _UserRoleDict = {
  "M": "manager",
  "N": "normal",
}
const UserRoleItems = prepare("common_const.user_role.", _UserRoleDict);

export {UserStatusItems, UserRoleItems}