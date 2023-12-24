package main

import (
	"fmt"
	"sort"
)

type Bundle struct {
	SKU      string
	ChildSKU string
}

func main() {
	bundles := []Bundle{}
	for r := 'A'; r < 'Z'; r++ {
		p := fmt.Sprintf("%c", r)
		n := fmt.Sprintf("%c", r+1)
		bundles = append(bundles, Bundle{
			SKU:      fmt.Sprintf("%v%v", p, n),
			ChildSKU: p,
		})
		bundles = append(bundles, Bundle{
			SKU:      fmt.Sprintf("%v%v", p, n),
			ChildSKU: n,
		})
	}
	fmt.Printf("%+v\n", bundles)

	related := findRelated(bundles, []string{"A", "B", "C", "D"})
	listRelated := []string{}
	for SKU := range related {
		listRelated = append(listRelated, SKU)
	}
	sort.Strings(listRelated)
	fmt.Println(listRelated)
}

func findRelated(bundles []Bundle, SKUs []string) map[string]bool {
	mapResult := map[string]map[string]bool{}
	for _, SKU := range SKUs {
		result, ok := mapResult[SKU]
		if !ok {
			result = findRelatedPerSKU(bundles, SKU, nil)
			for SKU := range result {
				mapResult[SKU] = result
			}
			fmt.Printf("%v new\n", SKU)
		} else {
			fmt.Printf("%v cached\n", SKU)
		}
	}

	result := map[string]bool{}
	for _, item := range mapResult {
		for SKU := range item {
			result[SKU] = true
		}
	}
	return result
}

func findRelatedPerSKU(bundles []Bundle, target string, visited map[string]bool) map[string]bool {
	if visited == nil {
		visited = map[string]bool{}
	}

	related := map[string]bool{}
	for _, bundle := range bundles {
		var nextRelated map[string]bool
		if bundle.SKU == target && !visited[bundle.ChildSKU] {
			visited[bundle.ChildSKU] = true
			related[bundle.ChildSKU] = true
			nextRelated = findRelatedPerSKU(bundles, bundle.ChildSKU, visited)
		} else if bundle.ChildSKU == target && !visited[bundle.SKU] {
			visited[bundle.SKU] = true
			related[bundle.SKU] = true
			nextRelated = findRelatedPerSKU(bundles, bundle.SKU, visited)
		}
		for SKU := range nextRelated {
			related[SKU] = true
		}

	}
	return related
}
