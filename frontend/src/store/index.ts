import { store } from 'quasar/wrappers'
import Vuex from 'vuex'

import collections from './collections'
import { CollectionsStateInterface } from './collections/state'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation
 */

export interface StateInterface {
  collections: CollectionsStateInterface;
}

export default store(function ({ Vue }) {
  Vue.use(Vuex)

  const Store = new Vuex.Store<StateInterface>({
    modules: {
      collections
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: !!process.env.DEV
  })

  return Store
})
