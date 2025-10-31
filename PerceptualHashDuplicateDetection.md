# Perceptual Hash Duplicate Detection: pHash & dHash Implementation

AiCatalog implements state-of-the-art perceptual hashing algorithms to identify near-duplicate images across massive photo collections. Unlike cryptographic hashes (SHA-256, MD5) that change completely with even minor pixel differences, perceptual hashes remain stable across similar images—detecting duplicates even when photos have been resized, slightly cropped, color-adjusted, or re-compressed.

## Two Complementary Algorithms

### pHash (Perceptual Hash - DCT-Based)

Our pHash implementation uses Discrete Cosine Transform (DCT) to analyze the frequency components of images, similar to JPEG compression. The algorithm:

1. Converts images to 32×32 grayscale for consistent analysis
2. Applies 2D DCT to transform spatial pixel data into frequency domain
3. Extracts the low-frequency 8×8 region (captures overall structure, ignores fine details)
4. Compares each frequency value to the median to generate a 64-bit hash

pHash excels at detecting duplicates with:
- **Rotation/crop tolerance**: Focuses on structural patterns rather than exact pixels
- **Compression artifacts**: Ignores high-frequency noise from JPEG re-encoding
- **Color adjustments**: Grayscale conversion makes it color-agnostic

### dHash (Difference Hash - Gradient-Based)

Our dHash implementation tracks brightness gradients across images. The algorithm:

1. Resizes images to 9×8 grayscale (9 columns to calculate 8 horizontal differences)
2. Compares each pixel to its immediate neighbor to capture directional brightness changes
3. Generates a 64-bit hash representing the gradient pattern (left brighter than right = 1, else = 0)

dHash excels at detecting duplicates with:
- **Speed**: ~3-5× faster than pHash due to simpler calculations
- **Minor edits**: Highly sensitive to structural changes while tolerating exposure shifts
- **Aspect ratio changes**: Gradient patterns remain recognizable across mild distortions

## BK-Tree Optimization for Scalable Search

Rather than comparing each image hash against every other hash (O(n²) complexity), AiCatalog implements a **Burkhard-Keller Tree** (BK-Tree)—a metric space data structure optimized for Hamming distance calculations.

### How It Works

- Organizes perceptual hashes in a tree structure where child nodes are grouped by their Hamming distance from parents
- Uses the **triangle inequality** property to prune entire subtrees during search
- Reduces similarity search from O(n) to approximately O(log n) for large catalogs

### Performance Impact

- **500K photo catalog**: Traditional brute-force = ~125 billion comparisons → BK-Tree = ~19 operations per query
- **Memory efficient**: ~64 bytes per hash node
- **Batch optimization**: Supports concurrent multi-hash lookups with shared tree traversal

## Hamming Distance & Similarity Scoring

Both algorithms produce 64-bit hashes compared using **Hamming distance**—the count of differing bits. Lower distance = higher similarity:

- **Distance 0-5**: Identical or virtually identical (same photo, different format)
- **Distance 6-10**: Very similar (minor edits, crops, or adjustments)
- **Distance 11-15**: Similar structure (same scene, different processing)
- **Distance 16+**: Different images

AiCatalog classifies matches into **confidence levels**:

- **High Confidence** (distance ≤ 8): Safe to auto-suggest as duplicates
- **Medium Confidence** (distance 9-12): Likely duplicates, user verification recommended
- **Low Confidence** (distance 13-15): Possible duplicates, requires manual review

## Real-World Applications

### Primary Use Cases

1. **Storage optimization**: Identify near-duplicates to reclaim disk space (showing potential space savings per group)
2. **Archive cleanup**: Detect multiple versions of edited photos (RAW + JPG pairs, bracketed shots)
3. **Backup verification**: Confirm files remain intact across drives despite metadata changes
4. **Collection deduplication**: Clean up years of accumulated photos with auto-detection of similar shots

### Workflow Integration

- Batch processing with configurable thresholds (hamming distance: 5-15)
- User verification UI with side-by-side comparison
- Selective deletion: Keep best quality (largest file size) or manual selection
- CSV export for audit trails and external processing

## Technical Performance

Benchmarks on M2 Pro (16GB RAM):

- **pHash generation**: ~15-25ms per image (DCT calculation intensive)
- **dHash generation**: ~3-5ms per image (simple gradient comparison)
- **Similarity search** (500K catalog): <100ms per query with BK-Tree
- **Memory footprint**: ~32MB for 500K perceptual hashes (8 bytes × 500K × 2 algorithms)

Both algorithms run on background threads using `Accelerate.framework` for optimized matrix operations, ensuring the UI remains responsive during batch processing of thousands of images.

---

**Technical Implementation:** Swift 5.9, AppKit + Accelerate, GRDB.swift for hash storage, concurrent processing with GCD.
