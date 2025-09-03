import { render, screen } from '@testing-library/react'
import { describe, it, expect, vi } from 'vitest'
import { ImageCounter } from '../components/ImageCounter'

// Mock the API calls
vi.mock('../api', () => ({
  checkApiStatus: vi.fn().mockResolvedValue({ status: 'healthy' }),
  countObjects: vi.fn(),
  getPerformanceMetrics: vi.fn(),
}))

describe('ImageCounter', () => {
  it('renders without crashing', () => {
    render(<ImageCounter />)
    expect(screen.getByText(/AI Object Counter/i)).toBeInTheDocument()
  })

  it('displays upload area', () => {
    render(<ImageCounter />)
    expect(screen.getByText(/Drop an image here/i)).toBeInTheDocument()
  })

  it('shows object type selection', () => {
    render(<ImageCounter />)
    expect(screen.getByText(/Object Type/i)).toBeInTheDocument()
  })
})
