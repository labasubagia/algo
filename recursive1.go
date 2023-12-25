package main

import (
	"fmt"
	"sort"
	"unicode"
)

type Bundle struct {
	SKU      string
	ChildSKU string
}

func main() {
	bundles := []Bundle{}
	for r := 'a'; r < 'z'; r++ {
		p := fmt.Sprintf("%c", unicode.ToUpper(r))
		n := fmt.Sprintf("%c", unicode.ToUpper(r+1))
		bundles = append(bundles, Bundle{
			SKU:      fmt.Sprintf("%v%v", p, n),
			ChildSKU: p,
		})
		bundles = append(bundles, Bundle{
			SKU:      fmt.Sprintf("%v%v", p, n),
			ChildSKU: n,
		})
	}

	bundles = append(bundles, Bundle{
		SKU:      "1_2",
		ChildSKU: "1",
	})

	bundles = append(bundles, Bundle{
		SKU:      "1_2",
		ChildSKU: "2",
	})

	fmt.Printf("%v\n", bundles)

	related := findRelated(bundles, []string{"A", "B", "XY", "1_2"})
	sort.Strings(related)
	fmt.Println(related)
}

func findRelated(bundles []Bundle, SKUs []string) []string {
	resultMap := map[string]map[string]struct{}{}
	for _, SKU := range SKUs {
		result, ok := resultMap[SKU]
		if !ok {
			result = findRelatedPerSKU(bundles, SKU, nil)
			for SKU := range result {
				resultMap[SKU] = result
			}
			fmt.Printf("%v new\n", SKU)
		} else {
			fmt.Printf("%v cached\n", SKU)
		}
	}

	agg := map[string]struct{}{}
	for _, item := range resultMap {
		for SKU := range item {
			agg[SKU] = struct{}{}
		}
	}

	related := []string{}
	for SKU := range agg {
		related = append(related, SKU)
	}
	return related
}

func findRelatedPerSKU(bundles []Bundle, target string, acc map[string]struct{}) map[string]struct{} {
	if acc == nil {
		acc = map[string]struct{}{}
	}
	for _, bundle := range bundles {
		if _, ok := acc[bundle.ChildSKU]; bundle.SKU == target && !ok {
			acc[bundle.ChildSKU] = struct{}{}
			acc = findRelatedPerSKU(bundles, bundle.ChildSKU, acc)
		} else if _, ok := acc[bundle.SKU]; bundle.ChildSKU == target && !ok {
			acc[bundle.SKU] = struct{}{}
			acc = findRelatedPerSKU(bundles, bundle.SKU, acc)
		}

	}
	return acc
}
