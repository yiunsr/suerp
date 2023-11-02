let cookie = {
  // https://stackoverflow.com/a/38699214
  setCookie: function(name, value, hours = 2, path = '/'){
    const expires = new Date(Date.now() + hours * 2 * 60 * 60 * 1000).toUTCString()
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=' + path
  },
  deleteCookie: function(name, path = '/'){
    cookie.setCookie(name, '', -1, path)
  },
  getCookie: function(name){
    return document.cookie.split('; ').reduce((r, v) => {
      const parts = v.split('=')
      return parts[0] === name ? decodeURIComponent(parts[1]) : r
    }, '')
  },

};

const getCookie = (name) => {
  return document.cookie.split('; ').reduce((r, v) => {
    const parts = v.split('=')
    return parts[0] === name ? decodeURIComponent(parts[1]) : r
  }, '')
}
export {cookie}
