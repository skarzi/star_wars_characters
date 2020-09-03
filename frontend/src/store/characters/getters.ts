import { GetterTree } from 'vuex'
import { StateInterface } from '../index'
import { CharactersStateInterface } from './state'

const getters: GetterTree<CharactersStateInterface, StateInterface> = {
  someAction (/* context */) {
    // your code
  }
}

export default getters
