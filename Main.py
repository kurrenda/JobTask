import Data,DataMan,DataWoman, ApiReader, UploadFile, DownloadFile
from argparse import ArgumentParser


def main():

    ap = ArgumentParser()
    ap.add_argument('filename')
    ap.add_argument('-mode')
    ap.add_argument('-year', type= int)
    ap.add_argument('-prov')
    ap.add_argument('-prov2')
    ap.add_argument('-gender', default='default')




    args = ap.parse_args()

    name = args.filename

    if args.filename == 'api':
        ApiReader.api()

    if args.filename == 'uploadfile':
        UploadFile.upload()

    if args.filename == 'downloadfile':
        DownloadFile.download()

    if args.mode == 'zad1':
        year = int(args.year)
        if args.gender == 'default':
            answer = Data.Count(name)
            answer.average(year,args.prov)
        if args.gender == 'kobiety':
            answer = DataWoman.CountWoman(name)
            answer.average(year,args.prov)
        if args.gender == 'mezczyzni':
            answer = DataMan.CountMan(name)
            answer.average(year,args.prov)

    if args.mode == 'zad2':

        year = int(args.year)
        if args.gender == 'default':
            answer = Data.Count(name)
            answer.percentPrint(year,args.prov)
        if args.gender == 'kobiety':
            answer = DataWoman.CountWoman(name)
            answer.percentPrint(year,args.prov)
        if args.gender == 'mezczyzni':
            answer = DataMan.CountMan(name)
            answer.percentPrint(year,args.prov)

    if args.mode == 'zad3':
        year = int(args.year)
        if args.gender == 'default':
            answer = Data.Count(name)
            answer.bestPass(year)
        if args.gender == 'kobiety':
            answer = DataWoman.CountWoman(name)
            answer.bestPass(year)
        if args.gender == 'mezczyzni':
            answer = DataMan.CountMan(name)
            answer.bestPass(year)

    if args.mode == 'zad4':
        if args.gender == 'default':
            answer = Data.Count(name)
            answer.bestProvince()
        if args.gender == 'kobiety':
            answer = DataWoman.CountWoman(name)
            answer.bestProvince()
        if args.gender == 'mezczyzni':
            answer = DataMan.CountMan(name)
            answer.bestProvince()


    if args.mode == 'zad5':
        answer = Data.Count(name)
        if args.gender == 'default':
            answer.compareProvince(args.prov, args.prov2)
        if args.gender == 'kobiety':
            answer = DataWoman.CountWoman(name)
            answer.compareProvince(args.prov, args.prov2)
        if args.gender == 'mezczyzni':
            answer = DataMan.CountMan(name)
            answer.compareProvince(args.prov, args.prov2)



if __name__=="__main__":
    main()