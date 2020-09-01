package main
import "fmt"


func intersect(nums1 []int, nums2 []int) []int {
    temp := map[int]int{}
    for _,val :=range nums1{
        temp[val] +=1
    }
    k := 0
    for _,v := range nums2{
        if temp[v] > 0{
            temp[v] -= 1
            
            nums2[k] = v
            k++
        }
    }
    return nums2[0:k]
}

func main (){
	var t1 = []int{1,2,3,4,2}
	var t2 = []int{2,9,2}
	var a = intersect(t1,t2)
	fmt.Println(a)
	
}