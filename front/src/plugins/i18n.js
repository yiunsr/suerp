import lang_csv from "@/assets/csv/i18n.csv?raw";
import { createI18n } from 'vue-i18n'

function parseCsv(csv){
  let lines = csv.split(/\r?\n/);
  let csvJson = [];
  let header = lines[0].split(",");
  lines = lines.slice(1);
  for(const line of lines){
    let cols = line.split(",");
    let item = {};
    for(let colidx in cols){
      let key = header[colidx];
      let col = cols[colidx];
      item[key] = col;
    }
    csvJson.push(item);
  }
  return csvJson;
}

let langs = parseCsv(lang_csv);

let en_dict = {}
let ko_dict = {}
let key_dict = {}
for(let item of langs){
  let key = item["key"]
  en_dict[key] = item["en"]
  ko_dict[key] = item["ko"]
  key_dict[key] = key;
}


const messages = {
  en: {
    ...en_dict
  },
  ko: {
    ...ko_dict
  },
  key: {
    ...key_dict
  }
};



export const i18n = new createI18n({
  legacy: false,
  locale: 'ko', // set locale
  messages
});
