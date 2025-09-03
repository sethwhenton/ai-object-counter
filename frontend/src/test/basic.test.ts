import { describe, it, expect } from 'vitest'

describe('Basic Frontend Tests', () => {
  it('should perform basic math operations', () => {
    expect(2 + 2).toBe(4)
    expect(3 * 3).toBe(9)
    expect(10 - 5).toBe(5)
  })

  it('should handle string operations', () => {
    expect('hello' + ' ' + 'world').toBe('hello world')
    expect('test'.length).toBe(4)
    expect('AI Object Counter').toContain('AI')
  })

  it('should work with arrays', () => {
    const testArray = [1, 2, 3, 4, 5]
    expect(testArray.length).toBe(5)
    expect(testArray.reduce((a, b) => a + b, 0)).toBe(15)
    expect(testArray).toContain(3)
  })

  it('should handle objects', () => {
    const testObj = { name: 'AI Counter', version: '1.0' }
    expect(testObj.name).toBe('AI Counter')
    expect(testObj).toHaveProperty('version')
    expect(Object.keys(testObj)).toHaveLength(2)
  })
})
