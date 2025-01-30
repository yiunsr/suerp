import _ from 'lodash';
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
  for (const [key, value] of Object.entries(dict)) {
      items.push({
        title: prefix + value, 
        str: prefix==""? "":i18n.global.t(prefix + value),
        value: key, value_int: parseInt(key),
      })
  }
  return items;
}

function strSubtitle(item){
  return {title: item.str, subtitle: item.substr}
}

function prepareWithSub(prefix_title, prefix_subtitle, dict){
  let items = [];
  for(const key in dict){
    let value = dict[key];
    const title = prefix_title + value;
    const str = prefix_title==""? "":i18n.global.t(prefix_title + value);
    const subtitle = prefix_subtitle + value;
    const substr = prefix_subtitle==""? "":i18n.global.t(prefix_subtitle + value);
    items.push({title, str, value, subtitle, substr})
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

const _ColMetaColumnMetaDict = {
  1: "data_jb", 2: "tags_jb", 
  3: "category_data_jb",
  4: "category_tags_jb",
}

const ColMetaColumnMetaItems = computed(() => {
  return prepare("", _ColMetaColumnMetaDict);
});

const _ColMetaDataTypeDict = {
  "n": "n", "m": "m", "d": "d", "f": "f", "c": "c", "s": "s",
  "b": "b", "D": "D", "t": "t", "T": "T", "e": "e", "M": "M",
}
const ColMetaDataTypeItems = computed(() => {
  return prepareWithSub(
    "page_col_meta.data_type_", 
    "page_col_meta.data_type_subtitle_", 
    _ColMetaDataTypeDict);
});



const _ColMetaVisibleDict = {
  0: "hide_all",
  1: "show_list",
  2: "show_detail",
  3: "show_all"
}
const ColMetaVisibleItems = computed(() => {
  return prepare("page_col_meta.visible.", _ColMetaVisibleDict);
});

const _ColMetaHTMLTypeDict = {
  date: "date", time: "time", datetime: "datetime",
  number: "number", text: "text", textarea: "textarea", 
  autocomplete:"autocomplete", radio: "radio", 
  select: "select",
  checkbox: "checkbox",
}
const ColMetaHTMLTypeItems = prepare("", _ColMetaHTMLTypeDict);


export {reverseItem, strSubtitle,
  UserStatusItems, UserRoleItems, 
  ColMetaStateItems, ColMetaTableItems, ColMetaColumnMetaItems, ColMetaDataTypeItems,
  ColMetaVisibleItems, ColMetaHTMLTypeItems
}
