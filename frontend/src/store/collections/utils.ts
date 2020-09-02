import { Collection } from '../../components/models'
import { RawCollection } from './interfaces'

export function processCollection (rawCollection: RawCollection) : Collection {
  return {
    id: rawCollection.id,
    createdAt: new Date(rawCollection.created_at)
  }
}
