import { Character } from '../../components/models'
import { RawCharacter } from './interfaces'
import { snakeToCamel } from '../../strings'

interface StringToStringMap {
  [key: string]: string;
}

export function processCharacter (rawCharacter: RawCharacter) : Character {
  const character = {} as Character
  for (const [key, value] of Object.entries(rawCharacter)) {
    character[snakeToCamel(key)] = String(value)
  }
  return character
}
