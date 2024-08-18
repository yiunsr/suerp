import {i18n} from '@/plugins/i18n';
import { computed } from 'vue';

function _getItemByValue(items, value){
  for(const item of items){
    if(item.value == value){
      return item;
    }
  }
  return null;
}

function reverseItem(items, value){
  if(!value) return "";
  let item = _getItemByValue(items, value);
  if(!item) return "";
  return i18n.global.t(item.title);
}

function prepare(prefix, dict){
  let items = [];
  for(const key in dict){
    let value = dict[key];
    items.push({
      title: prefix + value, 
      str: i18n.global.t(prefix + value),
      value: key
    })
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
const UserStatusItems = computed(() => {
  return prepare("common_const.status.", _UserStatusDict);
});

const _UserRoleDict = {
  "M": "manager",
  "N": "normal",
}
const UserRoleItems = computed(() => {
  return prepare("common_const.user_role.", _UserRoleDict);
});

const _ColMetaStateDict = {
  "A": "available",
  "S": "system",
  "D": "deleted",
  "U": "unusable",
  "H": "hidden",
}
const ColMetaStateItems = computed(() => {
  return prepare("common_const.status.", _ColMetaStateDict);
});
const _ColMetaTableDict = {
  1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
}
const ColMetaTableItems = computed(() => {
  return prepare("page_col_meta.table_", _ColMetaTableDict);
});




export {reverseItem, UserStatusItems, UserRoleItems, ColMetaStateItems, ColMetaTableItems,}