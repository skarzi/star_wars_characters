import { ActionTree } from 'vuex'
import { StateInterface } from '../index'
import { CollectionsStateInterface } from './state'
import {
  AxiosPeopleCollectionResponse,
  AxiosCreatePeopleCollectionResponse
} from './interfaces'

const actions: ActionTree<CollectionsStateInterface, StateInterface> = {
  async fetchCollection (context, concreteURL = '') {
    /* eslint-disable
      @typescript-eslint/no-unsafe-call,
      @typescript-eslint/no-unsafe-assignment,
      @typescript-eslint/no-unsafe-member-access
    */
    const response = await this._vm.$peopleAPI.get<AxiosPeopleCollectionResponse>(
      concreteURL || 'collections/people/'
    )
    console.log('Collection Fetched!')
    console.log(response)
    context.commit('processCollections', response.data.data)
    context.commit('setNextPage', response.data.next || '')
    context.commit('setTotalCount', response.data.count)
    /* eslint-enable */
  },
  async createCollection (context) {
    /* eslint-disable
      @typescript-eslint/no-unsafe-call,
      @typescript-eslint/no-unsafe-assignment,
      @typescript-eslint/no-unsafe-member-access
    */
    const response = await this._vm.$peopleAPI.post<AxiosCreatePeopleCollectionResponse>(
      'collections/people/'
    )
    context.commit('appendCollection', response.data.data)
    /* eslint-enable */
  }
}

export default actions
