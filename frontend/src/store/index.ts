import { store } from 'quasar/wrappers'
import Vuex from 'vuex'

import collections from './collections'
import characters from './characters'
import { CollectionsStateInterface } from './collections/state'
import { CharactersStateInterface } from './characters/state'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation
 */

export interface StateInterface {
  collections: CollectionsStateInterface;
  characters: CharactersStateInterface;
}

export default store(function ({ Vue }) {
  Vue.use(Vuex)

  const Store = new Vuex.Store<StateInterface>({
    modules: {
      collections,
      characters
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: !!process.env.DEV
  })

  return Store
})
