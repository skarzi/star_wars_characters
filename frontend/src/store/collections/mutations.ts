import { MutationTree } from 'vuex'
import { CollectionsStateInterface } from './state'
import { RawCollection } from './interfaces'
import { processCollection } from './utils'

const mutation: MutationTree<CollectionsStateInterface> = {
  processCollections (
    state: CollectionsStateInterface,
    rawCollections: Array<RawCollection>
  ) {
    const collections = rawCollections.map(processCollection)
    state.collections = [...collections, ...state.collections]
    state.wasRequestSent = true
  },
  appendCollection (
    state: CollectionsStateInterface,
    rawCollection: RawCollection
  ) {
    state.collections = [processCollection(rawCollection), ...state.collections]
    state.totalCount += 1
  },
  setTotalCount (state: CollectionsStateInterface, newTotalCount: number) {
    state.totalCount = newTotalCount
  },
  setNextPage (state: CollectionsStateInterface, newNextPage: string) {
    state.nextPage = newNextPage
  }
}

export default mutation
