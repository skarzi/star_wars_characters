<template>
  <q-page class="row items-start justify-evenly">
    <q-table
      row-key="name"
      title="file.csv"
      :data="characters"
      :columns="columns"
      :loading="isLoading"
      :pagination.sync="pagination"
      color="primary"
      table-header-class="text-weight-bold text-uppercase"
      card-class="bg-black text-primary"
      flat
      square
    >
      <template v-slot:bottom>
        <q-space />
        <div class="q-pa-md">
          <q-btn
            @click="loadMoreCharacters"
            label="Load more"
            icon="cloud_download"
            :disabled="!nextPage"
          />
        </div>
        <q-space />
      </template>
    </q-table>
  </q-page>
</template>

<script lang="ts">
import { Character } from 'components/models'
import { Vue, Component } from 'vue-property-decorator'
import { createNamespacedHelpers } from 'vuex'

const charactersNamespace = createNamespacedHelpers('characters')

@Component({
  computed: charactersNamespace.mapState([
    'characters',
    'totalCount',
    'nextPage'
  ]),
  methods: charactersNamespace.mapActions([
    'fetchCharacters'
  ])
})
export default class CollectionDetail extends Vue {
  // state
  characters!: Character[]
  totalCount!: number
  nextPage!: string
  // actions
  fetchCharacters!: () => Promise<void>

  isLoading = false
  columns = [
    { name: 'name', field: 'name', label: 'Name' },
    { name: 'height', field: 'height', label: 'Height' },
    { name: 'hairColor', field: 'hairColor', label: 'Hair Color' },
    { name: 'eyeColor', field: 'eyeColor', label: 'Eye Color' },
    { name: 'birthYear', field: 'birthYear', label: 'Birth Year' },
    { name: 'gender', field: 'gender', label: 'Gender' },
    { name: 'homeworld', field: 'homeworld', label: 'Homeworld' },
    { name: 'date', field: 'date', label: 'Date' }
  ]

  pagination = {
    page: 1,
    rowsPerPage: 10,
    rowsNumber: 0
  }

  async created () {
    await this.fetchCharacters(`collections/people/${this.$route.params.id}`)
  }

  async loadMoreCharacters () {
    if (this.nextPage) {
      this.isLoading = true
      await this.fetchCharacters(this.nextPage)
      this.pagination.rowsPerPage += 10
      this.pagination.rowsNumber = this.totalCount
      this.isLoading = false
    }
  }
}
</script>
