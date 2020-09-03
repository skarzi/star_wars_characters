<template>
  <q-page class="row items-start justify-evenly">
    <div class="q-my-md col-xs-10">
      <div class="row">
        <div class="col-xs-8">
          <div class="text-primary text-left text-h4">
            Collections
            <span class="q-ml-md text-caption">
              {{ collections.length }} / {{ totalCount }}
            </span>
          </div>
        </div>
        <div class="col-xs-4 text-right">
          <q-btn
            label="Fetch"
            color="primary"
            text-color="black"
            :loading="isCreating"
            @click="createNewCollection()"
          />
        </div>
      </div>
    </div>
    <div class="col-xs-10">
      <q-infinite-scroll
        @load="loadMoreCollections"
        debounce="300"
        :initial-index="collections.length"
      >
        <collection-list :collections="collections"></collection-list>
      </q-infinite-scroll>
    </div>
  </q-page>
</template>

<script lang="ts">
import { Collection } from 'components/models'
import CollectionList from 'components/CollectionListComponent.vue'
import { Vue, Component } from 'vue-property-decorator'
import { createNamespacedHelpers } from 'vuex'

const collectionsNamespace = createNamespacedHelpers('collections')

@Component({
  components: { CollectionList },
  computed: collectionsNamespace.mapState([
    'wasRequestSent',
    'collections',
    'totalCount',
    'nextPage'
  ]),
  methods: collectionsNamespace.mapActions([
    'fetchCollection',
    'createCollection'
  ])
})
export default class PageIndex extends Vue {
  // state
  wasRequestSent!: boolean
  collections!: Collection[]
  totalCount!: number
  nextPage!: string
  // actions
  fetchCollection!: () => Promise<void>
  createCollection!: () => Promise<void>

  isCreating = false

  async loadMoreCollections (index, done) {
    const shouldStop = this.wasRequestSent && !this.nextPage
    if (!shouldStop) {
      await this.fetchCollection(this.nextPage)
    }
    // eslint-disable-next-line @typescript-eslint/no-unsafe-call
    done(shouldStop)
  }

  async createNewCollection () {
    this.isCreating = true
    await this.createCollection()
    this.isCreating = false
  }
}
</script>
