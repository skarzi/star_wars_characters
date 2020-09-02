import axios, { AxiosInstance } from 'axios'
import { boot } from 'quasar/wrappers'

declare module 'vue/types/vue' {
  interface Vue {
    $axios: AxiosInstance
    $peopleAPI: AxiosInstance
  }
}

export default boot(({ Vue }) => {
  // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
  Vue.prototype.$axios = axios
  // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
  Vue.prototype.$peopleAPI = axios.create({
    // TODO: load it from env
    baseURL: 'http://localhost:8000'
  })
})
