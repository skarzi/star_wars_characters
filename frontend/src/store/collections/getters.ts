import { GetterTree } from 'vuex'
import { StateInterface } from '../index'
import { CollectionsStateInterface } from './state'

const getters: GetterTree<CollectionsStateInterface, StateInterface> = {
  someAction (/* context */) {
    // your code
  }
}

export default getters
