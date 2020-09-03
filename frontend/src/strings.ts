export function snakeToCamel (name: string) : string {
  return name.replace(
    /([-_][a-z])/g,
    (group) => group.toUpperCase().replace('-', '').replace('_', '')
  )
}
