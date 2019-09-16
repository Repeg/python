import axios from 'axios'
axios.defaults.withCredentials = true
axios.defaults.timeout = 15000
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'

let apiUrl = 'http://127.0.0.1:5000'

const PostRequest = (url, params, callback) => axios({
    method: 'POST',
    url: apiUrl + url,
    data: params,
    transformRequest: [function(data) {
      let ret = ''
      for (let it in data) {
        ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
      }
      return ret
    }],
  }).then(function(response) {
    callback(response.data)
  })
  .catch(function(error) {
    let str = error + ''
    if (str.search('timeout') !== -1) {   // 超时error捕获
      console.error('timeout_POST')
    }
    if(str.search('Network Error') !== -1){
      console.error('网络连接失败，请稍后重试')
    }
  })

const getRequest = (url, params, callback) => axios.get(apiUrl + url, {
    params: params,
    transformRequest: [function(data) {
      let ret = ''
      for (let it in data) {
        ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
      }
      return ret
    }],
  })
  .then(function(response) {
    callback(response.data)
  })
  .catch(function(error) {
    let str = error + ''
    if (str.search('timeout') !== -1) {   // 超时error捕获
      console.error('timeout_GET')
    }
    if(str.search('Network Error') !== -1){
      console.error('网络连接失败，请稍后重试')
    }
  });

export const login = (params, callback) => PostRequest('/login', params, callback)
export const logout = (params, callback) => PostRequest('/logout', params, callback)

// export const goodsSellAmount = (params, callback) => getRequest('/goods/sellAmount/', params, callback)