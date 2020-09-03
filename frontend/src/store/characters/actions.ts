import { ActionTree } from 'vuex'
import { StateInterface } from '../index'
import { CharactersStateInterface } from './state'
import { AxiosCharactersResponse } from './interfaces'

const actions: ActionTree<CharactersStateInterface, StateInterface> = {
  async fetchCharacters (context, url: string) {
    /* eslint-disable
      @typescript-eslint/no-unsafe-call,
      @typescript-eslint/no-unsafe-assignment,
      @typescript-eslint/no-unsafe-member-access
    */
    const response = await this._vm.$peopleAPI.get<AxiosCharactersResponse>(
      url
    )
    context.commit('processCharacters', response.data.data)
    context.commit('setNextPage', response.data.next || '')
    context.commit('setTotalCount', response.data.count)
    context.commit('setMeta', response.data.meta)
    /* eslint-enable */
  },
  clearCharactersData (context) {
    context.commit('clearCharactersData')
  }
}

export default actions
