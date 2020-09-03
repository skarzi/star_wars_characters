import { Module } from 'vuex'
import { StateInterface } from '../index'
import state, { CharactersStateInterface } from './state'
import actions from './actions'
import getters from './getters'
import mutations from './mutations'

const collectionsModule: Module<CharactersStateInterface, StateInterface> = {
  namespaced: true,
  actions,
  getters,
  mutations,
  state
}

export default collectionsModule
