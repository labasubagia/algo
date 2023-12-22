package main

import (
	"reflect"
	"sort"
	"testing"
)

type Bundle struct {
	SKU      string
	ChildSKU string
}

// https://go.dev/play/p/iKACFpYdYxk
func TestFindRelated(t *testing.T) {
	bundles := []Bundle{
		{SKU: "AB", ChildSKU: "A"},
		{SKU: "AB", ChildSKU: "B"},

		{SKU: "BC", ChildSKU: "B"},
		{SKU: "BC", ChildSKU: "C"},

		{SKU: "DE", ChildSKU: "D"},
		{SKU: "DE", ChildSKU: "E"},

		{SKU: "ABC", ChildSKU: "A"},
		{SKU: "ABC", ChildSKU: "B"},
		{SKU: "ABC", ChildSKU: "C"},

		{SKU: "ABCD", ChildSKU: "A"},
		{SKU: "ABCD", ChildSKU: "B"},
		{SKU: "ABCD", ChildSKU: "C"},
		{SKU: "ABCD", ChildSKU: "D"},
	}
	target := "A"
	expected := []string{"AB", "BC", "DE", "ABC", "ABCD", "A", "B", "C", "D"}

	related, _ := findRelated(bundles, target, nil)
	actual := []string{}
	for SKU := range related {
		actual = append(actual, SKU)
	}
	sort.Strings(actual)

	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("test related failed")
	}
}

func findRelated(bundles []Bundle, target string, visited map[string]bool) (map[string]bool, int) {
	if visited == nil {
		visited = map[string]bool{}
	}

	related := map[string]bool{}
	step := 0
	for _, bundle := range bundles {
		var nextRelated map[string]bool
		var nextStep int
		if bundle.SKU == target && !visited[bundle.ChildSKU] {
			visited[bundle.ChildSKU] = true
			related[bundle.ChildSKU] = true
			nextRelated, nextStep = findRelated(bundles, bundle.ChildSKU, visited)
		} else if bundle.ChildSKU == target && !visited[bundle.SKU] {
			visited[bundle.SKU] = true
			related[bundle.SKU] = true
			nextRelated, nextStep = findRelated(bundles, bundle.SKU, visited)
		}
		for SKU := range nextRelated {
			related[SKU] = true
		}
		step++
		step += nextStep

	}
	return related, step
}
