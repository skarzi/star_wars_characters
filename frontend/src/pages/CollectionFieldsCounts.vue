<template>
  <q-page class="row items-start justify-evenly q-py-md">
    <q-table
      row-key="name"
      :data="fieldsCounts"
      :columns="columns"
      :loading="isLoading"
      :pagination.sync="pagination"
      color="primary"
      card-class="bg-black text-primary"
      table-header-class="text-weight-bold text-uppercase"
      hide-bottom
      hide-pagination
      flat
      square
    />
  </q-page>
</template>

<script lang="ts">
import { FieldCount } from 'components/models'
import { Vue, Component } from 'vue-property-decorator'

export interface FieldsCountsResponse {
  data: Array<FieldCount>
}

export interface AxiosFieldsCountsResponse {
  data: FieldsCountsResponse
  status: number
}

export interface ColumnConfig {
  name: string
  field: string
  label: string
}

@Component
export default class CollectionFieldsCounts extends Vue {
  isLoading = false

  fieldsCounts: Array<FieldCount> = []

  pagination = {
    page: 1,
    rowsPerPage: 10,
    rowsNumber: 0
  }

  get columns () {
    const columns = this.$route.params.fieldNames.split(',').map(
      (fieldName: string) : ColumnConfig => {
        return {
          name: fieldName,
          field: fieldName,
          label: fieldName
        }
      }
    )
    columns.push({ name: 'count', field: 'count', label: 'count' })
    return columns
  }

  async created () {
    this.isLoading = true
    await this.fetchFieldsCounts()
    this.pagination.rowsPerPage = this.fieldsCounts.length
    this.pagination.rowsNumber = this.fieldsCounts.length
    this.isLoading = false
  }

  async fetchFieldsCounts () {
    const response = await this.$peopleAPI.get<AxiosFieldsCountsResponse>(
      `collections/people/${this.$route.params.id}/counts/${this.$route.params.fieldNames}/`
    )
    this.fieldsCounts = response.data.data
  }
}
</script>
