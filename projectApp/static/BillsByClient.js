$(document).ready(function (){



                  //Get query result on submit
            $('#send_bill_client').on('click', function(e){


                e.preventDefault();
                var bill_client=document.getElementById("bill_client").value;

                $.ajax({
                        type: "GET",
                        url:"http://127.0.0.1:5000//ajax/get_bills_by_client",
                        data: {bill_client:bill_client},
                        success:function(response){

                        var table = ""

                        console.log(response.bill_info)

                        //change result title
                            var resultTitle=document.getElementById("ResultTitle")
                            resultTitle.innerText="Result for: "+ bill_client

                        for (i = 0; i < response.bill_info.length; i++){
                            bill = response.bill_info[i]
                            console.log(bill)


                            table += `<tr>
                                <td id="billID">${bill.billID}</td>
                                <td id="buyerName">${bill.buyerName}</td>
                                <td id="makerResult">${bill.maker}</td>
                                <td id="modelResult">${bill.model}</td>
                                <td id="trimResult">${bill.cartrim}</td>
                                <td id="colorResult">${bill.carcolor}</td>
                                <td id="yearResult">${bill.caryear}</td>
                                <td id="conditionResult">${bill.condition}</td>
                                <td id="mileageResult">${bill.mileage}</td>
                                <td id="weightResult">${bill.carweight}</td>
                                <td id="priceResult">${bill.price}</td>
                                </tr>`
                        }

                        $("#resulttable tbody").html(table)

                        },
                        error : function(response){
                            console.log("It's not working")
                            console.log(response)
                         }
            })
            })
        });


